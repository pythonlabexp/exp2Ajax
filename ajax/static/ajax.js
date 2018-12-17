var req;

function sendRequest(suggest){
	if(window.XMLHttpRequest){
		req= new XMLHttpRequest();
	}
	
	var url="/sugestion/"+suggest;
	req.onreadystatechange=getResponse;
	req.open("POST",url,true);
	req.send();
}

function getResponse(){
	if (req.readyState==4){
		if (req.status==200){
			
			document.getElementById("suggestions").innerHTML=req.responseText;
		}
	}	
}

