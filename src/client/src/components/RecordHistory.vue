<template>
  <v-container>
     <v-layout align-center justify-center wrap="true">
      <v-card class="record" dark
        v-for="item in state.records" @click="setActiveRecId(item.id)" :key="item.id" >
        <v-card-title>
          <div>
            <h4>Request: {{ item.id }}</h4>
            <p>{{ item.originalText.substring(0, 25) }}</p>
          </div>
        </v-card-title>
      </v-card>
      </v-layout>
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
  .record {
    min-height: 50px;
    min-width: 80px;
    margin: 10px;
    cursor: pointer;
    border: 1px solid black;
    text-align: center;
  }
</style>
