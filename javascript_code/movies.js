// handle button clicked event
const btn = document.querySelector('button');
const input = document.querySelector('input');
const posterImg = document.getElementById('poster');
const titleEle = document.getElementById('title');
const yearEle = document.getElementById('year');
const nameEle=document.getElementById('name');

const timeEle=document.getElementById('time');
const actorsEle=document.getElementById('actors');
const directorEle=document.getElementById('director');

/*
{Title: 'RRR', Year: '2022', Rated: 'Not Rated', Released: '25 Mar 2022', Runtime: '187 min', …}
Actors
: 
"N.T. Rama Rao Jr., Ram Charan, Ajay Devgn"
Awards
: 
"Won 1 Oscar. 83 wins & 150 nominations total"
BoxOffice
: 
"$15,156,051"
Country
: 
"India"
DVD
: 
"22 May 2022"
Director
: 
"S.S. Rajamouli"
Genre
: 
"Action, Drama"
Language
: 
"Hindi, Malayalam, Portuguese, Tamil, Kannada, Korean, Turkish, Spanish, Telugu, English"
Metascore
: 
"83"
Plot
: 
"A fearless warrior on a perilous mission comes face to face with a steely cop serving British forces in this epic saga set in pre-independent India."
Poster
: 
"https://m.media-amazon.com/images/M/MV5BODUwNDNjYzctODUxNy00ZTA2LWIyYTEtMDc5Y2E5ZjBmNTMzXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg"
Production
: 
"N/A"
Rated
: 
"Not Rated"
Ratings
: 
(3) [{…}, {…}, {…}]
Released
: 
"25 Mar 2022"
Response
: 
"True"
Runtime
: 
"187 min"
Title
: 
"RRR"
Type
: 
"movie"
Website
: 
"N/A"
Writer
: 
"Vijayendra Prasad, S.S. Rajamouli, Sai Madhav Burra"
Year
: 
"2022"
imdbID
: 
"tt8178634"
imdbRating
: 
"7.8"
imdbVotes
: 
"165,437"
*/


//https://www.omdbapi.com/?t=rrr&apikey=3bbc63d6

function get_url(value) {
    return `https://www.omdbapi.com/?t=${value}&apikey=3bbc63d6`
}

btn.addEventListener("click",()=>{
    // when user clicks on the button, then get the value of the input field and show a alert message
    const value = input.value.trim()
    if (value === "") {
        alert("Movie name cannot be empty")
        return
    } 
    const url = get_url(value);

    fetch(url)
        .then((resp) => {
            return resp.json()
        })
        .then((data) => {
            console.log(data);
            //once data is here update the UI
            // first: update the poster

            posterImg.src = data.Poster
            titleEle.innerText = data.Title
            yearEle.innerText=data.Year
            nameEle.innerText = data.Genre
            timeEle.innerText = data.Runtime
            actorsEle.innerText = data.Actors
            directorEle.innerText = data.Director
           
 
        })
        .catch((err) => {
            console.log(err);
    })
    
     
    
})