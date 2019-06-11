<template>
  <v-container>
    <v-form>
      <v-checkbox v-model="removeStopWords" label="Remove stop words?"></v-checkbox>

      <v-flex xs12 class="text-xs-center text-sm-center text-md-center text-lg-center">
        <v-text-field label="Select text" @click='pickFile' v-model='fileName' prepend-icon='attach_file'></v-text-field>
        <input
          type="file"
          style="display: none"
          ref="filePicker"
          accept=".txt"
          @change="onFilePicked"
          >
      </v-flex>

        <v-btn color="info" @click='submit'>Submit</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    title: 'Text Upload',
    fileName: '',
    textUrl: '',
    textFile: '',
    removeStopWords: true,
    formData: new FormData(),
  }),

  methods: {
    pickFile() {
      this.$refs.filePicker.click();
    },

    onFilePicked (e) {
      const files = e.target.files;
      if(files[0] !== undefined) {

        if(files.length > 0) {
          // pick 0
          this.fileName = files[0].name;
          this.formData.append('file', files[0], this.fileName);
        }

        // load with filereader to peek inside?
      } else {
        this.resetFrom();
      }
    },

    async submit() {
      try {
        // TODO run before submission tasks
        this.formData.append('removeStopWords', this.removeStopWords);
        await this.uploadFormData();
      } catch (e) {
        console.log(e);
        alert(e); // WARN blocks ui
      }
    },

    async uploadFormData() {
      let { data } = await axios.post(store.serverAddress+'/analysis', this.formData);
      return data;
    },

    resetFrom() {
      this.fileName = '';
      this.textFile = '';
      this.textUrl = '';
      this.formData = new FormData();
    },

  }
}
</script>

<style>

</style>
