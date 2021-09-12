function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$(".like__button").click(function(e) {
    if(user_authenticated == "True") {
        if($(`.${e.target.classList[2]}`)[0].innerHTML == 'favorite_border') {
            const id = e.target.classList[2].split('-')[1]
            $(`.${e.target.classList[2]}`)[0].innerHTML = 'favorite'
            $(`.${e.target.classList[2]}`).addClass('add-color')

            $.ajax({
                type: 'GET', 
                url: `/post/like/${id}/`,
                success: function(response) {
                    console.log(response)
                    if(response['status']) {
                        alertify.success('Event added to liked list');
                    } else {
                        alertify.error('Server Error! Try again');
                    }
                },
                error: function(err) {
                    console.log(err)
                    alertify.error('Server Error! Try again');
                }
            })

        } else {
            const id = e.target.classList[2].split('-')[1]
            $(`.${e.target.classList[2]}`)[0].innerHTML = 'favorite_border'
            $(`.${e.target.classList[2]}`).removeClass('add-color')

            $.ajax({
                type: 'GET', 
                url: `/post/unlike/${id}/`,
                success: function(response) {
                    console.log(response)
                    if(response['status']) {
                        alertify.warning('Event removed from liked list');
                    } else {
                        alertify.error('Server Error! Try again');
                    }
                },
                error: function(err) {
                    console.log(err)
                    alertify.error('Server Error! Try again');
                }
            })
        }
    } else {
        alertify.error('Sign in is required'); 
    }
})