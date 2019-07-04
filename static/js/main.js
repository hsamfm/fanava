// background slider
const slider = [
    "/static/img/slider-1.jpg",
    "/static/img/slider-2.jpg",
    "/static/img/slider-3.jpg",
    "/static/img/slider-4.jpg",
    "/static/img/slider-5.jpg"
];
let counter = 2;
$(document).ready(function () {
    setInterval(function () {
        $(".Home").css('background', 'url(' + slider[counter] + ') no-repeat');
        $(".Home").css('background-size', 'cover');
        $(".Home").css('background-position', 'center');

        counter++;
        if (counter == slider.length) {
            counter = 1;
        }
    }, 3000);
})

// navbar background 
$(window).on("scroll", function () {
    if ($(window).scrollTop() > 50) {
        $(".main-nav").addClass("change-color");
        $(".navbar-nav").addClass("short-menu");
    } else {
        //remove the background property so it comes transparent again (defined in your css)
        $(".main-nav").removeClass("change-color");
        $(".navbar-nav").removeClass("short-menu");
    }
});
// sign Up change steps
const changeStep = function (now, go, percent) {
    $(".step" + now).css("display", "none");
    $(".step" + go).css("display", "block");
    $("#progress-step").css("width", percent + "%")
}
// forget pass
$(".forget-box button").on("click", function () {
    $(".send-pass").text("رمز عبور جدید برای شما ارسال شد.");
    $(".send-pass").addClass("text-success");
    $(".resend-pass").text("ارسال مجدد رمز عبور");
    $(".resend-pass").addClass("text-info");
});
$(".resend-pass").on("click", function () {
    $(".send-pass").text("رمز عبور مجددا برای شما ارسال شد.");
});


$(".product-list .sup-list-title").on("click", function () {
    $(">i", this).toggleClass("fa-plus");
    $(">i", this).toggleClass("fa-window-minimize");
    // $(this).children(".sub-list").css("display","block");
    $(this).next().toggleClass("com-height");
})
$(".fa-chevron-right").on("click", function () {

})
// $(".new-products fa-chevron-right").on("click",function() {
//     var product_cards =document.getElementsByClassName("product-card");
//     var i;
//     for(i=0 ; i<product_cards.length ; i++){
//         product_cards[i].removeClass("order-"+(i));
//         product_cards[i].addClass("order-"+(i+1));
//     }
//     product_cards[product_cards.length].removeClass("order-"+(i+1));
//     product_cards[product_cards.length].addClass("order-0");
// })

$(".new-products fa-chevron-right").on("click", function () {
    $(".slider-products-section >div").css(" transform", "translateX(100%)")
})