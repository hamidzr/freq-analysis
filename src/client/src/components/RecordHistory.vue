<template>
  <v-container>
    <v-list>
      <template v-for="item in state.records">
        <li :key="item.id" @click="setActiveRecId(item.id)">{{ item.id }}</li>
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
    await this.fetchRecords();
  },

  methods: {
    async fetchRecords() {
      try {
        let { data } = await axios.get(store.serverAddress+'/analysis');
        data = data.sort((a,b) => a.id > b.id ? -1 : 1);
        this.state.records = data;
        this.state.activeRecId = data[0].id;
        return data;
      } catch(e) {
        console.log(e);
      }
    },

    setActiveRecId(id) {
      this.state.activeRecId = id;
    }
  }
}
</script>

<style>

</style>
