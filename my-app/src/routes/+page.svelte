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
        <div class="rectangle">
        <h2>
            Upload Your Wardrobe!
        </h2>
        <button on:click>
        Click me
    </button>
        </div>
    
        <div class="rectangle2">
            
        </div>
    </div>
    
    <style>
        button {
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
        .root {
            position: relative;
            width: 1440px;
            height: 540px;
            align-items: flex-start;
            background-color: #fff;
            overflow: hidden;
        }
        
        .rectangle {
            position: absoulte;
            left: 0;
            top: 0;
            width: 1440px;
            height: 200px;
            background-color: #ffcfd4;
        }
        .rectangle2 {
            position: absolute;
            left: 0;
            top: 440px;
            width: 1440px;
            height: 100px;
            background-color: #afd1a0;
        }
        
        h2 {
            //position: relative;
            width: 38.5%;
            //height: 300vh;
            color: rgb(220,113,43);
            text-align: center;
            padding: 1.5em 0.5em 0.5em 0.5em;
            box-sizing: border-box;
            pointer-events: none;
        }
    </style>