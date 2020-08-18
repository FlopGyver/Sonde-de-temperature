<!doctype html>     
<html lang="fr">    
<head>     
             
  <meta charset="utf-8">                        
  <title>Sonde de température</title>                    
  <link rel="stylesheet" href="index.css">
  <link rel="icon" type="image/png" href="images/irupfavicon.png">
  <link rel="stylesheet" href="./style.css">      
  
  <script src="jquery.js"></script>             
  <script src="highcharts.js"></script>         
  <script src="gray.js"></script>               
  <script src="graphe.js"></script>     
  <script src="http://code.jquery.com/jquery-latest.js" > </script>
  <script>
 var refreshId = setInterval(function()
 {
      $('#result').fadeOut("slow").load('temp.php').fadeIn("slow");
 }, 5000);
 var result =0;
 </script>
         
</head>            

<body style="background-color: #2C2C2C">              
    
<h1 style="font-size:300%;">Sonde de Température</h1>

<!--GAUGES-->

<div class="gauge-container">
    <div id="result" style="font-size:200%;"></div>
</div>

<!--Graph-->
<script src="app.js"></script>
<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
<div id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div> 
<script type="text/javascript"></script>
<script  type="text/javascript" >


$(document).ready(function () {
    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    Highcharts.chart('container', {
        chart: {
            type: 'spline',
            animation: Highcharts.svg,
            marginRight: 10,
            events: {
                load: function () {

                    var series = this.series[0]; var r = 1;
                    setInterval(function () {
                        var x = (new Date()).getTime(), 
                            y = result;
                        series.addPoint([x, y], true, true);
                       
                    }, 30000);
                }
            }
        },
        title: {
            text: 'Local serveur Copernic'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150
        },
        yAxis: {
            title: {
                text: 'Température  °C'
            },
            plotLines: [{
                value: 0,
                width: 4,
                color: '#808080'
            }]
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                    Highcharts.numberFormat(this.y, 2);
            }
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        series: [{
            name: 'Copernic',
            data: (function () {
                
                var data = [],
                    time = (new Date()).getTime(),
                    i;

                for (i = -19; i <= 0; i += 1) {
                    data.push({
                        x: time + i * 1000,
                        y: 25
                    });
                }
                return data;
            }())
        }]
    });
});
		</script>
        
        
        
</body>             
</html>            
