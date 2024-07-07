var currentQuestion=0;
var currentSelectedOption = []; //[undefined,undefined,undefined,undefined,undefined]

const questions = [{
    "question": "what is the capital of India?",
    "options" : ["delhi", "gujarat","goa","punjab"],
    "answer" : "delhi"
 },
 {  "question": "2. what is capital of goa?",
    "options" : ["bangalore", "panaji","punjab","Chandigarh"],
    "answer" : "panaji"
 },
 {  "question": "3. what is capital of  Arunachal Pradesh",
    "options" : ["gandhi nagar", "punjab","Eeta Nagar","none of above"],
    "answer" : "Eeta Nagar"
},
{  "question": "4. what is capital of nagaland?",
   "options" : ["bangalore", "kohima","punjab","shillong"],
   "answer" : "kohima"
 },
 {  "question": "2. what is capital of Jammu- Kashmir?",
    "options" : ["Sri nagar", "panaji","delhi","simla"],
    "answer" : "Sri nagar"
}]
// based on the number of questions we should have that many current selected options
// below code will create an array of undefined values based on the number of questions
for(let i = 0; i<questions.length; i++){
    currentSelectedOption.push(undefined)
}




const nextButton = document.getElementById('next');
const previousButton = document.getElementById('previous');
const questionEle=document.getElementById('question');
const optionsEle=document.getElementById('options');
const optionItems=document.querySelectorAll('.option-item');
const currentQuestionEle=document.getElementById('current-question');
const totalQuestionEle=document.getElementById('total-questions');
const questionCircle=document.getElementById('question-circle ')


totalQuestionEle.innerText=questions.length;


const selectOption = (element)=> {
    removeActiveClasses()
    element.classList.toggle("bg-teal-100")
    element.classList.toggle('bg-teal-500')

    const option=parseInt(element.getAttribute("data-option"));
    currentSelectedOption[currentQuestion]=option;
}


nextButton.addEventListener("click",function() {
    //below code is to check if the current question is the last question
    // if it is last question then we should not d anything
    if(currentQuestion===questions.length-1){
        return;
        
    }
    removeActiveClasses()
    currentQuestion++;
    currentQuestionEle.innerText=currentQuestion+1;


    if(currentQuestion>0){
        previousButton.classList.remove("bg-indigo-500/50")
        previousButton.classList.add("bg-indigo-500")
    }
    
    
    
    let question=questions[currentQuestion];
    questionEle.innerText=question.question;

    // select all options-items and update the text with the options
    let optionItems=document.querySelectorAll('.option-item'); //div , div, div, div
    for(let i=0;i<optionItems.length;i++){
        let option=question.options[i];
        optionItems[i].innerText=option;
        if(currentSelectedOption[currentQuestion]===i){
            optionItems[i].classList.add("bg-teal-500")
        }
    }

    if (currentQuestion===questions.length-1){
        nextButton.classList.add("bg-indigo-500/50");
        nextButton.classList.remove("bg-indigo-500");
    }


})
previous.addEventListener("click", function(){
    if(currentQuestion===0){
        return;
    }
    currentQuestion--;

    removeActiveClasses()
    

    currentQuestionEle.innerText=currentQuestion+1;

    if(currentQuestion === 0){
        previousButton.classList.remove("bg-indigo-500")
        previousButton.classList.add("bg-indigo-500/50")
    } 

    let question=questions[currentQuestion];
    questionEle.innerText=question.question;
    // select all options-items and update the text  with the options
     //div , div, div, div
    for(let i=0;i<optionItems.length;i++){
        let option=question.options[i]; // delhi
        optionItems[i].innerText=option;
        if(currentSelectedOption[currentQuestion]===i){
            optionItems[i].classList.add("bg-teal-500")
        }
    } 
    if(currentQuestion===question.length-2){
        nextButton.classList.remove("bg-indigo-500/50")
        nextButton.classList.add("bg-indigo-500")
    }
     

})
