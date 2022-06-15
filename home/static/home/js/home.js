// if (document.location.pathname === '/') {
// 	let map = document.getElementById('osmap')
// 	map.addEventListener('', (event) =>{
// 		event.preventDefault()
// 		map.classList.toggle('enable')
// 	console.log(document.location.pathname === '/')
// 	})
// }

if (document.getElementById('main-search')){
	const searchInput = document.getElementById('search-input')
	const map = document.getElementById("osmap-scroll")

	searchInput.addEventListener('submit', (event) => {
		event.preventDefault()
	})
	if (map) {
		map.scrollIntoView({behavior: "smooth", block: "center"})
	}
}

