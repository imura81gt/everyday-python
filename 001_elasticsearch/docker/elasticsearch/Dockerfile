FROM elasticsearch:5.1

RUN bin/elasticsearch-plugin install analysis-icu
RUN bin/elasticsearch-plugin install analysis-kuromoji
RUN bin/elasticsearch-plugin install analysis-phonetic
#RUN bin/plugin install jetty

EXPOSE 9200

#ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]


