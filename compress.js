function compressString(str) {
   let rez = '';
   let count = 1;
   for(let i = 0; i < str.length; i++){
      let Old = str[i];
      let New = str[i + 1];
      if(Old === New){
         count++;
      }else{
         rez += Old + String(count);
         count = 1;
      };
   }
   return rez
}
