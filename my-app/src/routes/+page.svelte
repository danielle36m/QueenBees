<script>
    let files;
    
    $: if (files) {
        // Note that `files` is of type `FileList`, not an Array:
        // https://developer.mozilla.org/en-US/docs/Web/API/FileList
        console.log(files);

        for (const file of files) {
            console.log(`${file}`);
            //console.log(`${file.name}: ${file.size} bytes`);
        }

    }
</script>
    
<div class="root">
    <div class="pinkrectangle">
        <!-- <div class="topBar"> -->
        <div class="headerName">
            StyleForHue
        </div>
        <!-- </div> -->

        <h2>
            Upload Your Wardrobe
        </h2>
        <h5>
            Select your main piece of clothing to build your outfit!
        </h5>
        
        <input
        bind:files
        id="many"
        multiple
        type="file"
        />

        {#if files}
        <h2>Selected files:</h2>
        {#each Array.from(files) as file}
            <img class=image-size src={URL.createObjectURL(file)} alt="clothing">
        {/each}
        {/if}
        
        <button on:click>
        Submit Photos
        </button>
    </div>
</div>
    
<style>
    button {
        /* left: 10.8%; */
        height: 3rem;
        width: 6rem;
        background-color: #ffffff;
        border-color: #dd7729;
        color: #000000;
        font-size: 1.15rem;
        background-image: linear-gradient(45deg, #ef8635 50%, transparent 50%);
        background-position: 100%;
        background-size: 400%;
        transition: background 300ms ease-in-out;
    }
    button:hover {
        background-position: 0;
        color: #ffffff;
    }
    .root {
        width: 100%;
        height: 800px;
        background-color: #fff;
    }
    .pinkrectangle {
        height: 9%;
        background-color: #ffcfd4;
    }
    /* .topBar {
        top: 10%;
        left: 5%;
    } */
    .headerName {
        color: #fff7f7;
        font-size: 40px;
        line-height: 175%;
        font-weight: 500;
        font-family: Work Sans;
        left: 5%;
        padding: 0 .75em;
    }
    h2 {
        color: rgb(220, 113, 43);
        text-align: center;
        padding: 1.5em 0.5em 0.5em 0.5em;
    }
    h5 {
        color: rgb(220,113,43);
        text-align: center;
    }
    .image-size {
        width: 200px;
        height: 200px;
    }
    input[type="file"] {
        display: none;
    }
    label {
        display: inline-block;
        text-transform: uppercase;
        color: #fff;
        background: #ffcfd4;
        text-align: center;
        padding: 15px 40px;
        font-size: 18px;
        letter-spacing: 1.5px;
        user-select: none;
        cursor: pointer;
        box-shadow: 5px 15px 25px rgba(0, 0, 0, 0.35);
        border-radius: 3px; 
    }
    
</style>
