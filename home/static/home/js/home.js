if (document.location.pathname === '/') {
	let map = document.getElementById('osmap')
	map.addEventListener('change', (event) =>{
		event.preventDefault()
		map.classList.add('disabled')
	})
}

console.log(document.location.pathname === '/')