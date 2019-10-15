$('.js-next').on('click', function() {
	var current = $('.page.active');
	var findNext = $(current).next(".page");
	$(current).removeClass('active');
	setTimeout(function() {
		$(findNext).addClass("active");
	}, 200);
});

$('.js-prev').on('click', function() {
	var current = $('.page.active');
	var findPrev = $(current).prev(".page");
	$(current).removeClass('active');
	setTimeout(function() {
		$(findPrev).addClass("active");
	}, 200);
});

$('.js-back-to-1').on('click', function() {
	var current = $('.page.active');
	$(current).removeClass('active');
	setTimeout(function() {
		$('.page-cover').addClass("active");
	}, 400);
});
