<template>
  <v-container v-if="record">
    <p>showing record {{record.id}} </p>
    <ul>
      <li>id: {{ record.id }}</li>
      <li>removeStopWords?: {{ record.removeStopWords }}</li>
      <li>top words: {{ topWords(record) }}</li>
      <li>file: {{ record.originalText.substring(0, 50) }}</li>
    </ul>
    <p></p>
  </v-container>
</template>

<script>
export default {
  name: 'Record',
  data: () => {
    return {
      state: store.state,
    };
  },

  computed: {
    record() {
      return this.state.records
        .find(rec => rec.id == this.recordId);
    },
  },

  props: {
    recordId: {
      type: Number,
      default: 0
    }
  },

  created() {
  },

  methods: {
    topWords(rec) {
      return rec.wordCounts.slice(0, 25);
    }
  }
}
</script>

<style>

</style>
