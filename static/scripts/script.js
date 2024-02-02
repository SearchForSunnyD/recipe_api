const $results = $(".result_bucket");
const $more = $("#more");

async function load_more(evt) {
    evt.preventDefault();

    resp = await axios.get("/next");
    $results.html(resp.data)
}

$more.on("click", load_more);

