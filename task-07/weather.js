const API_KEY = "YOUR_API_KEY";
const API_URL = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox = document.getElementById("searchBox");
const searchButton = document.getElementById("searchButton");
const weatherDisplay = document.getElementById("weatherDisplay");
const tempLabel = document.getElementById("tempLabel");
const cityLabel = document.getElementById("cityLabel");
const statusLabel = document.getElementById("statusLabel");
const humidityLabel = document.getElementById("humidityLabel");
const windLabel = document.getElementById("windLabel");

const humidityIcon = document.getElementById("humidityIcon");
const humidityText = document.getElementById("humidityText");
const windIcon = document.getElementById("windIcon");
const windText = document.getElementById("windText");

async function fetchWeatherData(city) {
    try {
        const response = await fetch(`${API_URL}${city}&appid=${API_KEY}`);
        const data = await response.json();
        updateWeatherDisplay(data);
    } catch (error) {
        weatherDisplay.src = "none.png";
        tempLabel.innerHTML = "";
        cityLabel.innerHTML = "City not found!";
        statusLabel.innerHTML = "";
        humidityLabel.innerHTML = "";
        windLabel.innerHTML = "";
        humidityIcon.src="bgPlaceholder.png"
        humidityText.innerHTML = ""
        windIcon.src="bgPlaceholder.png"
        windText.innerHTML = ""
    }
}

function toTitleCase(str) {
    return str.replace(
      /\w\S*/g,
      function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
      }
    );
}

function updateWeatherDisplay(data) {
    cityLabel.innerHTML = data.name;
    tempLabel.innerHTML = Math.round(data.main.temp) + "°C";
    humidityLabel.innerHTML = data.main.humidity + "%";
    windLabel.innerHTML = data.wind.speed + " km/h";
    const status = data.weather[0].main;
    setWeatherDisplay(status);
    statusLabel.innerHTML = `${toTitleCase(data.weather[0].description)}`;
    humidityIcon.src="humidity.png"
    humidityText.innerHTML = "Humidity"
    windIcon.src="wind.png"
    windText.innerHTML = "Wind Speed"
}

function setWeatherDisplay(condition) {
    const iconMap = {
        "Clouds": "cloud.png",
        "Clear": "clear.png",
        "Rain": "rain.png",
        "Drizzle": "drizzle.png",
        "Haze": "haze.png",
        "Mist": "mist.png",
        "Smoke": "smoke.png",
        "Thunderstorm": "storm.png",
        "Dust": "dust.png",
        "Fog": "fog.png",
        "Sand": "sand.png",
        "Ash": "ash.png",
        "Squall": "tornado.png",
        "Tornado": "tornado.png",
        "Snow": "snow.png",
    };

    weatherDisplay.src = iconMap[condition] || "";
}

searchButton.addEventListener("click", () => {
    const city = searchBox.value;
    fetchWeatherData(city);
});

searchBox.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
      event.preventDefault();
      searchButton.click();
    }
  }); 
