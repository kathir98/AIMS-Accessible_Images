// Working code with save in local storage

document.getElementById('language_select').value=localStorage.getItem('selected_value')


const btn = document.getElementById("setlang");


	btn.addEventListener('click', ()=>{
        console.log("button clicked");
		let queryoptions = {active:true, currentWindow: true };
		chrome.tabs.query(queryoptions, (tabs)=>{
			console.log(tabs[0].id);
			var lang = document.querySelector('#language_select').value;
			console.log(lang);
			localStorage.setItem("selected_value",lang);

			var svalue = localStorage.getItem('selected_value');
	        console.log("lang "+svalue);
	        window.close();
            let language = {
		    a: svalue
	        };

            chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, language, function(response) {
            console.log(response);
            });
           });
		});
	});

var svalue = localStorage.getItem('selected_value');
	console.log("lang "+svalue);
    let language = {
		a: svalue
	};

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  chrome.tabs.sendMessage(tabs[0].id, language, function(response) {
    console.log(response);
  });
});


//let params = {
//    active: true,
//    currentWindow: true
//};
//chrome.tabs.query(params, gotTabs);
//
//function gotTabs(tabs) {
//
//	chrome.runtime.sendMessage(tabs[0].id, language);
//}



// ------------------------------------------------------------------------------------------------------













// ------------------------------------------------------------------------------------------------------

// // const btn = document.getElementById("setlang");

// // function doAction() {
// //     var images = document.getElementsByTagName('img'); 
// // 	images.crossOrigin = "Anonymous";
// // 	var srcList = [];
// // 	var alter = [];
// // 	var msg="";

// // 	for(var i = 0; i < images.length; i++) 
// // 	{
// // 	    if(images[i].alt===""||images[i].alt==='null')
// // 	    {
	        
// // 	        imgurl=images[i].src;
// // 	        console.log(imgurl);

// // 	        // msg=steg.decode(imgurl);
// // 	        // msg="hi kathir";

// // 	        if(msg!="")
// // 	        {
// // 	          images[i].setAttribute('alt', msg);
// // 	        }
	       
// // 	    }
// // 	}
// // 	return "success";
// // 	}


// // btn.addEventListener('click', async ()=>{

// // 	const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
// //     const tab = tabs[0]

// //     const scriptToExec = `(${doAction})()`;

// //     const scraped = await chrome.tabs.executeScript(tab.id, { code: scriptToExec });

// // });

// //-----------------------------------------------------------------------------
// // let bgpage= chrome.extension.getBackgroundPage();

// // let imgurl= bgpage.word;
// // let imgobj = bgpage.word1;

// // console.log(imgurl);
// // console.log(imgurl[0]);
// // console.log(imgobj[0]);

// // msg=steg.decode(imgurl[0]);
// // console.log(msg);

// //  if(msg!="")
// //  {
// //  	console.log("In msg block");
// // 	 imgobj[0].setAttribute('alt', 'hi');
// //  }

// //--------------------------------------------------------------------