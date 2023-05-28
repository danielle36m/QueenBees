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
        <div class="headerName">
            StyleForHue
        </div>
    </div>

    <div class="main">
        <div class="uploadWardrobe">
            Upload Your Wardrobe
        </div>
        <div class="description">
            Select your main piece of clothing to build your outfit!
        </div>

        <label for="many">Upload Clothing</label>
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
        <div class="submitPhotos">
            <button on:click>
                Submit Photos
            </button>
        </div>
        {/if}
        
        <!-- <div class="submitPhotos">
            <button on:click>
                Submit Photos
            </button>
        </div> -->
    </div>
</div>
    
<style>
    .center {
        align-self: center;
        place-items: center;
    }
    button {
        height: 3rem;
        width: 10rem;
        background-color: #ffcfd4;
        border-color: #f9dfe2;
        color: #ffffff;
        font-size: 1rem;
        text-transform: uppercase;
        background-image: linear-gradient(45deg, #ffffff 50%, transparent 50%);
        background-position: 100%;
        background-size: 400%;
        transition: background 300ms ease-in-out;
        transform: translateY(200%);
        border-radius: 4px; 
    }
    button:hover {
        background-position: 0;
        color: #ffcfd4;
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
    .headerName {
        color: #fff7f7;
        font-size: 40px;
        line-height: 175%;
        font-weight: 500;
        font-family: Work Sans;
        left: 5%;
        padding: 0 .75em;
    }
    .main {
        display: grid;
        place-items: center;
        /* justify-content: center;
        align-items: center; */
    }
    .uploadWardrobe {
        font-family: 'Crimson';
        font-size: 30px;
        font-weight: 600;
        text-align: center;
        padding: 1em 0.5em 0em 0.5em;
    }
    .description {
        width: 250px;
        font-family: 'Work Sans';
        font-size: 15px;
        font-weight: 100;
        text-align: center;
        padding: 1em 0.5em 2.25em 0.5em;
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
    .submitPhotos {
        position: relative;
        min-height: 100vh;
        
    }
    
</style>
