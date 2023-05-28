<script>
    let imageUrls = [
      'src/lib/images/image1.jpg',
      'src/lib/images/image2.jpg',
      'src/lib/images/image3.jpg'
    ];
</script>
  
<style>
.header {
    background-color: #F5DDE2; /* Pastel Pink */
    padding: 20px;
    text-align: center;
    font-family: Comic Sans MS;
}
.footer {
    background-color: #D3F0D0; /* Pastel Green */
    padding: 20px;
    text-align: center;
}

.content {
    background-color: #FFFFFF; /* White */
    padding: 20px;
    display: flex;
    justify-content: space-between;
}

.image {
    max-width: 30%;
}
</style>

<div class="header">
<h1>Your Results!</h1>
</div>

<div class="content">
{#each imageUrls as imageUrl}
    <img class="image" src={imageUrl} alt="Image" />
{/each}
</div>

<div class="footer">
<p>© 2023 StyleForHue. All rights reserved.</p>
</div>
  