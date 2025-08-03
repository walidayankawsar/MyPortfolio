// Function to toggle between dark and light modes
function toggleMode() {
    console.log('clicked');
    const body = document.body;
    body.classList.toggle('dark-mode');
    body.classList.toggle('light-mode');

    // Get the current mode
    const isDarkMode = body.classList.contains('dark-mode');

    // Update the CSS variables based on the mode
    document.documentElement.style.setProperty('--fontColor', isDarkMode ? '#6c757d' : 'black');
    document.documentElement.style.setProperty('--BGcolor', isDarkMode ? '#17191a' : 'white');

    // update nav 
    document.documentElement.style.setProperty('--navBG', isDarkMode ? '#242627' : '#eeeeee');

    // update the toggle icon 
    const toggleButton = document.getElementById('toggle-mode');
    if(isDarkMode) toggleButton.innerHTML = "<i class='fa-solid fa-sun' style='color: #ffc800;'></i>";
    else toggleButton.innerHTML = "<i class='fa-solid fa-moon'></i>";


    localStorage.setItem('mode', isDarkMode ? 'dark' : 'light');

    // fix the publatication list background color 
    const currentPagePath = window.location.pathname;
    if(currentPagePath == '/pages/publications.html'){
        fixPublicationBG();
    }
    
}
const modeToggleBtn = document.getElementById('toggle-mode');
modeToggleBtn.addEventListener('click', toggleMode);


const storedMode = localStorage.getItem('mode');
if (storedMode === 'light') {
    toggleMode();
}

// change thep ublication BG color
const fixPublicationBG = () => {
    const mode = localStorage.getItem('mode');
    if (mode == 'light') {
        document.getElementById('all-publications-ul').style.backgroundColor = '#eeeeee';
    }
    else{
        document.getElementById('all-publications-ul').style.backgroundColor = '#242627';
    }
}

