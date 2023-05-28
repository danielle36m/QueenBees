<script>
	import './styles.css';
</script>

<div class="app">

	<main>
		<slot />
	</main>

	<footer>
		<p>visit <a href="https://media.tenor.com/jUMex_rdqPwAAAAd/among-us-twerk.gif">StyleForHue</a> to learn more!</p>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
