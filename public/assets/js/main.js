new Vue({
  el: '#app',
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
        this.fileName = '';
        this.textFile = '';
        this.textUrl = '';
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
      let response = await axios.post('/analysis', this.formData);
    },

  }
});
