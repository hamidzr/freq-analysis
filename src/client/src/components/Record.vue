<template>
  <v-container>
    <p>record comp</p>
    <p>{{ record.id }} </p>
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
  }
}
</script>

<style>

</style>
