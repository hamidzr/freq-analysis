<template>
  <v-container v-if="record">
    <v-card>
      <v-card-title primary-title>
      <h3>Request: {{record.id}} </h3>
      <ul>
        <li>removeStopWords?: {{ record.removeStopWords }}</li>
        <li>top words: {{ topWords(record) }}</li>
      </ul>
      <v-card-actions>
          <v-btn flat color="orange" @click="downloadOriginalText">Original File</v-btn>
        </v-card-actions>
      </v-card-title>
    </v-card>
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
    },

    downloadOriginalText() {
      let fname = `record-${this.record.id}-originalText.txt`;
      this.download(fname, this.record.originalText);
    },

    download(filename, text) {

      let element = document.createElement('a');
      element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
      element.setAttribute('download', filename);

      element.style.display = 'none';
      document.body.appendChild(element);

      element.click();
      document.body.removeChild(element);
    }
  }
}
</script>

<style>

</style>
