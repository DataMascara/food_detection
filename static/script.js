n =  new Date();
var weekday = new Array(7);
weekday[0] = "Sunday";
weekday[1] = "Monday";
weekday[2] = "Tuesday";
weekday[3] = "Wednesday";
weekday[4] = "Thursday";
weekday[5] = "Friday";
weekday[6] = "Saturday";

var x = weekday[n.getDay()];
	
	var month = new Array();
month[0] = "January";
month[1] = "February";
month[2] = "March";
month[3] = "April";
month[4] = "May";
month[5] = "June";
month[6] = "July";
month[7] = "August";
month[8] = "September";
month[9] = "October";
month[10] = "November";
month[11] = "December";
var s = month[n.getMonth()];

d = n.getDate();

	
var da = document.querySelector('.date');

da.innerHTML = x + "," + s + " " + d ;


//////////////////////////////////////////////////////////////////////////////////

 const foodName = document.querySelector('#food')
      
       document.getElementById('getText').addEventListener('click', getPosts);


      function getPosts(e){

		 e.preventDefault();
        fetch(`https://api.nal.usda.gov/fdc/v1/foods/search?api_key=baL5VdKCuXYUKgY8CrDpVE38qPHCYobcog7kFUBf&query=${foodName.value}`)
    
         .then((response) => response.json())
         .then((data) => {
            let output = "";
            let arr;
            if(data.foods){
            data.foods.forEach(function(post){
            arr = post.foodNutrients;

            arr.forEach(function(todo){

              if(todo.nutrientName === "Energy"){

            output+=`

             <button class = "link" onclick="getCalories(${todo.value})">
            
            <h3>${post.description}<h3>


            <h4>${post.brandOwner}, 1 serving, ${todo.value} calories<h4>
          
             
            </button>
          

            `;
          
          }
  });

 });
          }
           
         document.getElementById('output2').innerHTML = output;
            
         })
      }


      ////////////////////////////////////////////////////////////////////////////

      function getCalories(x){
  
     let output2 = x;  
      
     document.getElementById('calories').innerHTML = output2;

      }

      ////////////////////////////////////////////////////////////////////////////


       function calculate(){
   
    var number = document.getElementById('number').innerHTML
    var calnumber = document.getElementById('calories').innerHTML
     let n = parseInt(number) ;
     let c = parseInt(calnumber);
     let calc = n - c;
    document.getElementById("number").innerHTML = calc;
}


//////////////////////////////////////////////////////////////////////////////////

