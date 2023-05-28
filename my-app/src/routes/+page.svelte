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
            <div class="barTopLeft">
                <div class="headerName">
                    StyleForHue
                </div>
            </div>
        </div>

        <h2>
            Upload Your Wardrobe!
        </h2>
        
        <!-- <button on:click>
        Click me
        </button> -->
        </div>
    
        <div class="greenrectangle">
            
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
            height: 1439px;
            align-items: flex-start;
            background-color: #fff;
            overflow: hidden;
        }
        
        .pinkrectangle {
            position: absoulte;
            left: 0;
            top: 0;
            width: 1440px;
            height: 658px;
            background-color: #ffcfd4;
        }
        .greenrectangle {
            position: absolute;
            left: 0;
            top: 1301px;
            width: 1440px;
            height: 138px;
            background-color: #afd1a0;
        }
        
        h2 {
            width: 100%;
            color: rgb(220,113,43);
            text-align: center;
            padding: 1.5em 0.5em 0.5em 0.5em;
            box-sizing: border-box;
            pointer-events: none;
            justify-content: center;
		    align-items: center;
		    padding: 12px;
        }
        .topBar {
            position: absolute;
            left: 135px;
            top: 66px;
            width: 1175px;
            height: min-content;
            place-content: space-between;
            align-items: center;
        }
        .barTopLeft {
            width: min-content;
            height: min-content;
            align-items: center;
            gap: 18px;
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
    </style>