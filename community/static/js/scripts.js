document.addEventListener("DOMContentLoaded", function () {
    fetch("/api/post/")  
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("posts-container");
            container.innerHTML = "";

            data.all_posts.forEach(post => {  
                const postElement = document.createElement("li");
                postElement.className = "list__post";
                postElement.id = "specific-post";
                postElement.tabIndex = 0;
                postElement.onclick = () => {
                    const featuredContainer = document.getElementById("featured-post");
                
                    featuredContainer.innerHTML = `
                        <img src="${post.image}" alt="${post.title}" class="featured__image">
                        <p class="post__user">By <span>${post.author}</span> | ${post.created_at}</p>
                        <h2 class="post__title">${post.title}</h2>
                        <p class="post__content">${post.content}</p>
                        <button class="primary-btn site-btn" onclick="window.location.href='/details/${post.id}/'">Read more</button>
                    `;
                };
                
                postElement.innerHTML = `
                    <p class="post__user">By <span>${post.author}</span> | ${post.created_at}</p>
                    <p class="post__title">${post.title}</p>
                `;
                container.appendChild(postElement);
            });
        })
});
