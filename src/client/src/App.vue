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
      <Record :recordId="state.activeRecId"/>
      <RecordHistory/>
    </v-content>
  </v-app>
</template>

<script>
import RecordHistory from './components/RecordHistory'
import RequestForm from './components/RequestForm'
import Record from './components/Record'

export default {
  name: 'App',
  components: {
    RecordHistory,
    RequestForm,
    Record,
  },

  data () {
    return {
      state: store.state,
    }
  }
}
</script>
