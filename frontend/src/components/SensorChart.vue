<template>
  <div>
    <h2>Temperature</h2>
    <div ref="tempChart"></div>

    <h2>Humidity</h2>
    <div ref="humidChart"></div>

    <h2>Air Quality</h2>
    <div ref="aqiChart"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sensorData: [],
    };
  },
  async mounted() {
    await this.loadCharts();
    await this.fetchData();
    setTimeout(() => this.renderCharts(), 300);
  },
  methods: {
    loadCharts() {
      return new Promise((resolve) => {
        if (window.google && window.google.charts) {
          window.google.charts.load("current", { packages: ["corechart"] });
          window.google.charts.setOnLoadCallback(resolve);
          return;
        }
        const script = document.createElement("script");
        script.src = "https://www.gstatic.com/charts/loader.js";
        script.async = true;
        script.onload = () => {
          window.google.charts.load("current", { packages: ["corechart"] });
          window.google.charts.setOnLoadCallback(resolve);
        };
        document.head.appendChild(script);
      });
    },

    async fetchData() {
      const response = await fetch("http://localhost:8000/sensor/processed/");
      this.sensorData = await response.json();
    },

    renderCharts() {
      this.renderTemperatureChart();
      this.renderHumidityChart();
      this.renderAirQualityChart();
    },

    renderTemperatureChart() {
      const el = this.$refs.tempChart;
      if (!el || this.sensorData.length === 0) return;

      const validData = this.sensorData.filter(
        (item) => item.timestamp && item.temperature !== undefined
      );
      if (validData.length === 0) return;

      const dataTable = new window.google.visualization.DataTable();
      dataTable.addColumn("datetime", "Time");
      dataTable.addColumn("number", "Temperature");
      dataTable.addColumn({ type: "string", role: "style" });

      const rows = validData.map((item) => [
        new Date(item.timestamp),
        item.temperature,
        item.temperature_outlier
          ? "point { color: red; size: 8; }"
          : "point { color: pink; }",
      ]);

      dataTable.addRows(rows);

      const chart = new window.google.visualization.ScatterChart(el);
      chart.draw(dataTable, {
        legend: { position: "none" },
        trendlines: { 0: {} },
      });
    },

    renderHumidityChart() {
      const el = this.$refs.humidChart;
      if (!el || this.sensorData.length === 0) return;

      const validData = this.sensorData.filter(
        (item) => item.timestamp && item.humidity !== undefined
      );
      if (validData.length === 0) return;

      const dataTable = new window.google.visualization.DataTable();
      dataTable.addColumn("datetime", "Time");
      dataTable.addColumn("number", "Humidity");
      dataTable.addColumn({ type: "string", role: "style" });

      const rows = validData.map((item) => [
        new Date(item.timestamp),
        item.humidity,
        item.humidity_outlier
          ? "point { color: red; size: 8; }"
          : "point { color: green; }",
      ]);

      dataTable.addRows(rows);

      const chart = new window.google.visualization.ScatterChart(el);
      chart.draw(dataTable, {
        legend: { position: "none" },
        trendlines: { 0: {} },
      });
    },

    renderAirQualityChart() {
      const el = this.$refs.aqiChart;
      if (!el || this.sensorData.length === 0) return;

      const validData = this.sensorData.filter(
        (item) => item.timestamp && item.air_quality !== undefined
      );
      if (validData.length === 0) return;

      const dataTable = new window.google.visualization.DataTable();
      dataTable.addColumn("datetime", "Time");
      dataTable.addColumn("number", "Air Quality");
      dataTable.addColumn({ type: "string", role: "style" });

      const rows = validData.map((item) => [
        new Date(item.timestamp),
        item.air_quality,
        item.air_quality_outlier
          ? "point { color: red; size: 8; }"
          : "point { color: blue; }",
      ]);

      dataTable.addRows(rows);

      const chart = new window.google.visualization.ScatterChart(el);
      chart.draw(dataTable, {
        legend: { position: "none" },
        trendlines: { 0: {} },
      });
    },
  },
};
</script>
