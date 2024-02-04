{% extends "base.html" %}

{% block content %}
<div class="container">
    {% for constellation in constellations %}
    {% if json_stars.items.constellation.id.0 == 1 %}
        <div class="cell">
            <img src="{{ constellation.image }}" alt="{{ constellation.latin_name_nom_latin }}" style="width: 100%; max-width: 300px;">
            <div class="info">
                <h3>{{ constellation.latin_name_nom_latin }}</h3>
                <p>Date/Time Found</p>
                <button onclick="openModal('{{ constellation.iau_code }}')">More Info</button>
            </div>
        </div>
    {% else %}
        <div class="cell">
            <img src="{{ constellation.image }}" alt="{{ constellation.latin_name_nom_latin }}" style="width: 100%; max-width: 300px;">
            <div class="info">
                <h3>{{ constellation.latin_name_nom_latin }}</h3>
                <p>Date/Time Found</p>
                <button onclick="openModal('{{ constellation.iau_code }}')">More Info</button>
            </div>
        </div>
    {% endif %}
    <!-- Enhanced Modal Structure -->
    <div id="constellationModal_{{ constellation.iau_code }}" class="modal">
        <div class="modal-content">
            <span onclick="closeModal('{{ constellation.iau_code }}')" class="close">&times;</span>
            <h2 id="modalTitle">{{ constellation.latin_name_nom_latin }}</h2>
            <!-- Place for more dynamic content -->
            <p id="modalInfo">IAU Code: {{ constellation.iau_code }}</p>
            <p id="modalInfo">English Name: {{ constellation.english_name_nom_en_anglais }}</p>
            <p id="modalInfo">Principal Star: {{ constellation.principal_star_etoile_principale }}</p>
            <p id="modalInfo">Right Ascension: {{ constellation.test }}</p>
            <p id="modalInfo">Declination: {{ constellation.dec_declinaison }}</p>
        </div>
    </div>
    {% endfor %}
</div>

<script>
    // Function to open the modal and populate it with constellation details
    function openModal(constellationId) {
        document.getElementById('constellationModal_' + constellationId ).style.display = "block";
    }

    function closeModal(constellationId) {
        var modal = document.getElementById('constellationModal_' + constellationId);
        var span = document.getElementsByClassName("close")[0];
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
</script>

<script>
const cursor = document.querySelector(".cursor");
const links = document.querySelectorAll("nav ul li a");
const navlinks = document.querySelectorAll("nav ul li");

document.addEventListener("mousemove", (e) => {
    let leftPosition = e.pageX + 4;
    let topPosition = e.pageY + 4;

    cursor.style.left = leftPosition + "px";
    cursor.style.top = topPosition + "px";
})

links.forEach(link => {
    link.addEventListener("mouseenter", () => {
        cursor.classList.add("large");
    })
})

links.forEach(link => {
    link.addEventListener("mouseleave", () => {
        cursor.classList.remove("large");
    })
})

// Animation

navlinks.forEach((li, i) => {
    li.style.animationDelay = 0 + i * 140 + "ms";
})</script>
{% endblock %}

