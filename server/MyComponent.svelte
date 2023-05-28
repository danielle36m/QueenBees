<script>
    
    function handlePhotoUpload(event){
        const photo = event.target.files[0];

        console.log("Uploaded photos:", photo)
    }
    
    // function selectPhoto() {}

    // function submitSelections() {}

   let files;

    $: if (files) {
        // Note that `files` is of type `FileList`, not an Array:
        // https://developer.mozilla.org/en-US/docs/Web/API/FileList
        console.log(files);

        for (const file of files) {
            console.log(`${file.name}: ${file.size} bytes`);
        }
    
</script>

<label for="many">Upload multiple photos:</label>
<input
	bind:photos
	id="many"
	multiple
	type="photo"
/>


