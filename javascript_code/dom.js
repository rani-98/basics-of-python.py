//get element by id: returns the element with the special Id.
const a = document.getElementById("root")
console.log(a);
a.innerHTML = "<a href='https://google.com'>Take me</a>"

// querySelector -> returns the first element that matches a specified CSS selector(s) in the document
const pTag = document.querySelector("p")
console.log(pTag);
pTag.textContent = "this is modified content"
pTag.style.backgroundColor = "black"
pTag.style.color = "white"

//querySelectorAll--> return all elements in the document that matches a specified css selectors.as a static nodelist object.
//syntax: document.queryselectorAll(selector)
const pTags = document.querySelectorAll("p")
console.log(pTags);

//i need to select all the p tags which have a class called"para"
//selector--> .para
const paraTags = document.querySelectorAll(".para")
console.log(paraTags);

//getElementByClassName-->returns a collection of all elements in the documents with the specified class name
const paraTags2 = document.getElementsByClassName("para")
console.log(paraTags2)


//let's select the div tag which have a class name  called"container"
//selector-->container
const container = document.querySelector(".container")
//let's create a h3 tag and appendit container
const newH3 = document.createElement("h3")
newH3.textcontent = "orange"
//add the h3 tag with container
container.appendChild(newH3)
//i want to select the third h3 tag inside the container
//selector : .container h3:nth-child(3)
const thirdH3 = document.querySelector(".container h3:nth-child(3")
//delete the third h3 tag 3rd element
thirdH3.remove()

















