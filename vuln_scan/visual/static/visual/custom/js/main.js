/**
 * Created by HappyMole on 4/12/18.
 */

function load_severity_chart(severity_summary) {
    var severity_option = {
        title: {
            text: "Severity Summary",
            left: "center"
        },
        tooltip: {
            trigger: "item",
            formatter: "{b} : {c} ({d}%)"
        },
        legend: {
            bottom: 10,
            left: "center",
            data: ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]
        },
        series: [
            {
                type: "pie",
                radius: "65%",
                selectedMode: "single",
                data: [
                    {value: severity_summary["HIGH"], name: "HIGH", itemStyle: {color: "#ed0036"}},
                    {value: severity_summary["MEDIUM"], name: "MEDIUM", itemStyle: {color: "#ffc200"}},
                    {value: severity_summary["LOW"], name: "LOW", itemStyle: {color: "#00a6bb"}},
                    {value: severity_summary["UNKNOWN"], name: "UNKNOWN", itemStyle: {color: "grey"}}
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
    var severity_chart = echarts.init(document.getElementById("severity_chart"));
    severity_chart.setOption(severity_option);
}

function load_vuln_count_chart(vuln_count) {
    var app_list = [], count_list = [];
    for (var app in vuln_count) {
        app_list.push(app);
        count_list.push(vuln_count[app]);
    }
    var vuln_count_option = {
        title: {
            text: "Application Summary",
            left: "center"
        },
        tooltip: {
            trigger: "item",
            formatter: "{b} : {c}"
        },
        legend: {
            bottom: 10,
            left: "center",
            data: ["Count"]
        },
        xAxis: {
            data: app_list
        },
        yAxis: {},
        series: [{
            name: "Count",
            type: "bar",
            data: count_list
        }]
    };
    var vuln_count_chart = echarts.init(document.getElementById("vuln_count_chart"));
    vuln_count_chart.setOption(vuln_count_option);
}