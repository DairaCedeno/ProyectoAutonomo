package com.example.demo.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.models.clienteModels;

@Repository
public interface ClienteRepositories extends CrudRepository<clienteModels>, Long {

    
}
