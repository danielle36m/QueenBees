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

<div class="pinktopback">
    <h2>
        Upload Your Wardrobe!
    </h2>
    <button on:click>
    Click me
</button>
    </div>

<div class="background">
    <label for="many">Upload Clothing</label>
    <input
        bind:files
        id="many"
        multiple
        type="file"
    />
    {#if files}
        <h2>Your Photos:</h2>
        {#each Array.from(files) as file}
            <img class=image-size src={URL.createObjectURL(file)} alt="clothing">
    {/each}
    {/if}
<div class="rectangle2"></div>
</div>

    <style>
        goupload {
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
        }
        .background {
            position: relative;
            width: 1440px;
            height: 540px;
            align-items: flex-start;
            background-color: #fff;
            overflow: hidden;
        }
        
        .pinktopback {
            position: absoulte;
            left: 0;
            top: 0;
            width: 1440px;
            height: 200px;
            background-color: #ffcfd4;
        }
        .footercolor {
            position: absolute;
            left: 0;
            top: 440px;
            width: 1440px;
            height: 100px;
            background-color: #afd1a0;
        }
        .image-size {
            width: 200px;
            height: 200px;
        }
        .many {
            text-align: center;
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
        /* h2 {
            //position: relative;
            width: 38.5%;
            //height: 300vh;
            color: rgb(220,113,43);
            text-align: center;
            padding: 1.5em 0.5em 0.5em 0.5em;
            box-sizing: border-box;
            pointer-events: none;
        } */
    </style>