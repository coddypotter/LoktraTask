$(document).ready(function(){

    var chkLocalStorage = chkLocalStorage();
    if(chkLocalStorage){
        //getCart();
    }else{
        alert('No localStorage support. Please upgrade your browser to latest versions.');
    }
    function chkLocalStorage(){
        if (typeof(Storage) !== "undefined") {
            // Code for localStorage.
            return true;
        } else {
            // Sorry! No Web Storage support..
            return false;
        }
    }

    $('.addToCart').click(function(){
        var quantity = 1,
            name = $(this).attr('data-name'),
            id = $(this).attr('data-pid'),
            price = $(this).attr('data-price');
        
        var p = [name, quantity, price];
        localStorage.setItem(id, JSON.stringify(p));
        Materialize.toast(name+" added to cart",4000);
    });    
});