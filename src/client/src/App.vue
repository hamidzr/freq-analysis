<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Frequency Analyzer</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-content>
      <RequestForm/>
      <ResultsTable/>
    </v-content>
  </v-app>
</template>

<script>
import ResultsTable from './components/ResultsTable'
import RequestForm from './components/RequestForm'

export default {
  name: 'App',
  components: {
    ResultsTable,
    RequestForm
  },
  data () {
    return {
      //
    }
  }
}
</script>
