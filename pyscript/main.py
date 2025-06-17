from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS
from datetime import datetime
import mysql.connector

# Load API key dari .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Inisialisasi Flask app
app = Flask(__name__)
CORS(app)


# Koneksi ke database RDS
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="weather-app-db.cd0ski4yk8q5.ap-southeast-2.rds.amazonaws.com",
            user="kelompok2",
            password="Walgondes0704",
            database="app",
        )
        return conn
    except Exception as e:
        print(f"❌ Gagal koneksi RDS: {e}")
        return None


# Root endpoint
@app.route("/")
def home():
    return "✅ Weather API Flask is running!"


# Endpoint cuaca
@app.route("/api/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Parameter 'city' wajib diisi."}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return jsonify(
                {
                    "error": data.get(
                        "message", "Gagal mengambil data dari OpenWeatherMap."
                    )
                }
            ), response.status_code

        result = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": round(data["main"]["temp"], 1),
            "feels_like": round(data["main"]["feels_like"], 1),
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "icon_code": data["weather"][0]["icon"],
        }

        # ✅ Simpan ke RDS
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                    INSERT INTO weather (
                        city, country, temperature, feels_like, humidity,
                        weather_description, wind_speed, icon_code
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(
                    query,
                    (
                        result["city"],
                        result["country"],
                        result["temperature"],
                        result["feels_like"],
                        result["humidity"],
                        result["weather_description"],
                        result["wind_speed"],
                        result["icon_code"],
                    ),
                )
                conn.commit()
                cursor.close()
            except Exception as db_err:
                print(f"❌ Gagal menyimpan ke RDS: {db_err}")
            finally:
                conn.close()

        # ✅ Ambil forecast 4 hari ke depan
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        today = datetime.now().strftime("%Y-%m-%d")
        daily_forecast = []
        for entry in forecast_data["list"]:
            if "12:00:00" in entry["dt_txt"] and entry["dt_txt"].split(" ")[0] != today:
                daily_forecast.append(
                    {
                        "date": entry["dt_txt"].split(" ")[0],
                        "temp": round(entry["main"]["temp"]),
                        "icon_code": entry["weather"][0]["icon"],
                    }
                )
                if len(daily_forecast) == 4:
                    break

        result["forecast"] = daily_forecast

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Jalankan server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
