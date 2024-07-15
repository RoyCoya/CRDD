export const getNodeText = (info) => {
    const onto = info.ontology;
    if (onto) {
        const onto_value = onto.value;
        if (onto_value) {
            if (typeof (onto_value) === 'object') return onto.title + '：' + onto_value.title;
            else return onto.title + '：' + onto_value;
        }
        else return onto.title;
        // + "：" + records.value.find((record) => {
        //     return record.id == info.record_id
        // }).text.substring(info.start, info.end);
    }
    else return 'Error: NOT FOUND ONTOLOGY'
};
