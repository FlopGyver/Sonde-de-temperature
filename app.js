var httpRequest = new XMLHttpRequest()

//debugger;

//var result = document.getElementById('result')

httpRequest.onreadystatechange = function() 
{
    var httpRequest = getHttpRequest()

    if (httpRequest.readyState === 4)
    {
        document.getElementById('result').innerHTML = httpRequest.responseText
        
        /*var results = JSON.parse(httpRequest.responseText)
        
        result.innerHTML =''
        var ul = document.creatElement('ul')
        results.appendChild(ul)
        for(var i = 0; i < results.lenght; i++) {
            
            var li = document.creatElement('li')
            
            li.innerHTML = results[i].name
            
            ul.appendChild(li) */
        
    }
}
return result
httpRequest.open('GET', './temp.php', true)
httpRequest.send()
$(form).fadeOut(800, function(){
    form.html(result).fadeIn().delay(2000);}
