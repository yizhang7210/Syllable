package com.syllable.exchange.events;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EventDao extends MongoRepository<ExchangeEvent, String> {
}
