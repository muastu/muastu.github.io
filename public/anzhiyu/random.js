var posts=["archives/2c336a21.html","archives/e01fbe6a.html","archives/6e476b7f.html","archives/4a17b156.html","archives/f1c538bd.html","archives/89e38926.html","archives/ddd4c2f4.html","archives/39c8ac7.html","archives/4ba7856f.html"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };