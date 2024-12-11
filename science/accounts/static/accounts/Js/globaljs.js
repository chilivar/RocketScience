document.addEventListener('DOMContentLoaded', () => {
    // Логика для логотипа
    const logoButton = document.querySelector('.logo-button');
    const videoModal = document.getElementById('videoModal');
    const closeModalLogo = videoModal?.querySelector('.close-modal');
    const modalVideo = document.getElementById('modalVideo');

    if (logoButton && videoModal && closeModalLogo && modalVideo) {
        // Открытие видео для логотипа
        logoButton.addEventListener('click', () => {
            videoModal.style.display = 'flex';
            modalVideo.play();
        });

        // Закрытие видео для логотипа
        closeModalLogo.addEventListener('click', () => {
            videoModal.style.display = 'none';
            modalVideo.pause();
            modalVideo.currentTime = 0;
        });

        // Закрытие при клике вне видео
        videoModal.addEventListener('click', (e) => {
            if (e.target === videoModal) {
                videoModal.style.display = 'none';
                modalVideo.pause();
                modalVideo.currentTime = 0;
            }
        });
    }

    // Логика для случайного видео
    const allButtons = document.querySelectorAll('button');
    const randomVideoModal = document.getElementById('randomVideoModal');
    const closeModalRandom = randomVideoModal?.querySelector('.close-modal');
    const randomModalVideo = document.getElementById('randomModalVideo');

    if (randomVideoModal && closeModalRandom && randomModalVideo) {
        allButtons.forEach(button => {
            button.addEventListener('click', () => {
                const randomChance = Math.floor(Math.random() * 5) + 1; // 20% вероятность
                if (randomChance === 1) {
                    randomVideoModal.style.display = 'flex';
                    randomModalVideo.play();
                }
            });
        });

        // Закрытие случайного видео
        closeModalRandom.addEventListener('click', () => {
            randomVideoModal.style.display = 'none';
            randomModalVideo.pause();
            randomModalVideo.currentTime = 0;
        });

        // Закрытие при клике вне видео
        randomVideoModal.addEventListener('click', (e) => {
            if (e.target === randomVideoModal) {
                randomVideoModal.style.display = 'none';
                randomModalVideo.pause();
                randomModalVideo.currentTime = 0;
            }
        });
    }

    // Логика для мемов
    const memesButton = document.getElementById('memesButton');
    const memesModal = document.getElementById('memesModal');
    const closeMemesModal = memesModal?.querySelector('.close-modal');
    const memeImage = memesModal?.querySelector('.meme-display');

    // Получение массива путей из JSON
    const memesArray = JSON.parse(document.getElementById('memes-data').textContent);

    if (memesButton && memesModal && closeMemesModal && memeImage) {
        // Открытие модального окна
        memesButton.addEventListener('click', () => {
            const randomIndex = Math.floor(Math.random() * memesArray.length);
            memeImage.src = memesArray[randomIndex];
            memesModal.style.display = 'flex';
        });

        // Закрытие модального окна
        closeMemesModal.addEventListener('click', () => {
            memesModal.style.display = 'none';
        });

        // Закрытие при клике вне окна
        memesModal.addEventListener('click', (e) => {
            if (e.target === memesModal) {
                memesModal.style.display = 'none';
            }
        });
    }

    //
    // function checkAuth() {
    //     const isLoggedIn = localStorage.getItem('isLoggedIn');
    //
    //     if (isLoggedIn === 'true') {
    //         document.getElementsByClassName('login-button').style.display = 'none';
    //         document.getElementsByClassName('register-button').style.display = 'none';
    //         document.getElementsByClassName('logout-button').style.display = 'inline-block';
    //     } else {
    //         document.getElementsByClassName('login-button').style.display = 'inline-block';
    //         document.getElementsByClassName('register-button').style.display = 'inline-block';
    //         document.getElementsByClassName('logout-button').style.display = 'none';
    //     }
    // }
    //
    //
    // const logoutButton = document.getElementsByClassName('logout-button');
    // if (logoutButton) {
    //     logoutButton.addEventListener('click', () => {
    //         localStorage.setItem('isLoggedIn', 'false');
    //         location.reload();
    //     });
    // }
    //
    //
    // checkAuth();
});
