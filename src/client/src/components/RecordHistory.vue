<template>
  <v-container>
    <v-list>
      <template v-for="(item, index) in state.records">
        <li :key="item.id">{{ item.id }}</li>
      </template>
    </v-list>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RecordHistory',
  data: () => {
    return {
      state: store.state,
    };
  },

  async created() {
    // let recs = await this.fetchRecords();
    // this.state.records = recs;
  },

  methods: {
    async fetchRecords() {
      let { data } = await axios.get('/analysis');
      return data;
    }
  }
}
</script>

<style>

</style>
