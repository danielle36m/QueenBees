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
        <div class="topBar">
            <div class="headerName">
                StyleForHue
            </div>
        </div>

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
        
        <!-- <button on:click>
        Click me
        </button> -->
    </div>
</div>
    
<style>
    /* button {
        position: relative;
        left: 15.8%;
        height: 3rem;
        width: 6rem;
        background-color: #aaa;
        border-color: #f1c40f;
        color: #f1c40f;
        font-size: 1.15rem;
        background-image: linear-gradient(45deg, #f1c40f 50%, transparent 50%);
        background-position: 100%;
        background-size: 400%;
        transition: background 300ms ease-in-out;
    }
    button:hover {
        background-position: 0;
        color: #aaa;
    } */
    .root {
        
        width: 100%;
        height: 1438px;
        align-items: flex-start;
        background-color: #fff;
        overflow: hidden;
    }
    .pinkrectangle {
       
        left: 0;
        top: 0;
        width: 100%;
        height: 9%;
        background-color: #ffcfd4;
    }
    .topBar {
        
        height: min-content;
        place-content: space-between;
        align-items: center;
    }
    .headerName {
        color: #fff7f7;
        font-size: 40px;
        line-height: 125%;
        font-weight: 500;
        font-family: Work Sans;
        width: min-content;
        height: min-content;
        white-space: nowrap;
        flex-direction: column;
    }
    h2 {

        color: rgb(220,113,43);
        text-align: center;
        padding: 1.5em 0.5em 0.5em 0.5em;
        box-sizing: border-box;
        pointer-events: none;
        justify-content: center;
        align-items: center;
        padding: 60px;
    }
    h5 {

        color: rgb(220,113,43);
        text-align: center;
        box-sizing: border-box;
        pointer-events: none;
        justify-content: center;
        align-items: center;
        padding: 70px;
    }
    .image-size {
        width: 200px;
        height: 200px;
    }
    
</style>