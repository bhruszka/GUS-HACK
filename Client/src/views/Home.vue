<template>
  <div class="home">

    <Fact v-for="fact in facts" :fact="fact" v-bind:key="fact.content" />
  </div>
</template>

<script>
// @ is an alias to /src
import Fact from "@/components/Fact.vue";

export default {
  data() {
    return {
      facts: [
        {content: "Szotuka była dyscypliną olimpijską od 1912 do 1948 roku", category: 1},
        {content: "10% ze wszystkich zdjęć istniejących na świecie zostało zrobione w ciągu ostatnich 12 miesięcy", category: 2},
        {content: "Co 10 mieszkaniec Centralnej Azji jest potomkiem Czyngis-chana", category: 1},
        {content: "W pewnej austriackiej wiosce znaki drogowe zrobione są z cementu, by zapobiec kradzieży", category: 3},
        {content: "Istnieje trzy razy większe ryzyko, że umrzemy w katastrofie lotniczej, niż zostaniemy zaatakowani przez pumę", category: 1},
        {content: "Jeśli rocznie zarabiasz więcej niż 64.000 złotych to należysz do 4% najbogatszych ludzi na świecie", category: 2},
        {content: "Kiedy „Mona Liza” została ukradziona z Luwru w 1911 roku, jednym z podejrzanych był Pablo Picasso", category: 4},
        {content: "W dniu urodzin ryzyko śmierci jest 14% większe niż w jakikolwiek inny dzień", category: 3},
        {content: "W książce Jerome K. Jerome „Trzech panów w łódce” pierwsze zdanie brzmi „Było nas czterech", category: 1},
        {content: "Ponad 7000 osób umiera, a 1.5 miliona ma problemy zdrowotne spowodowane nieczytelnym pismem lekarzy", category: 2},
        {content: "Większość diamentów ma ponad 3 miliardy lat", category: 4},
        {content: "Co 10 dziecko w Europie zostało poczęte w łóżku z IKEA", category: 3}
      ]
    };
  },
  name: "home",
  components: {
    Fact
  }
};
</script>
