document.addEventListener('DOMContentLoaded', function() {
    var menuItems = document.querySelectorAll('.dropdown-content a');

    menuItems.forEach(function(item) {
        item.addEventListener('click', function(event) {
            event.preventDefault();

            var selectedTag = this.textContent.trim().toLowerCase();
            if (selectedTag === 'all') {
                showAllCards();
            } else {
                filterCardsByTag(selectedTag);
            }
        });
    });

    function filterCardsByTag(tag) {
        var cards = document.querySelectorAll('.card-link');

        cards.forEach(function(card) {
            var tags = card.dataset.tags.split(',').map(function(tag) {
                return tag.trim().toLowerCase();
            });

            if (tags.includes(tag)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    function showAllCards() {
        var cards = document.querySelectorAll('.card-link');
        cards.forEach(function(card) {
            card.style.display = 'block';
        });
    }
});
