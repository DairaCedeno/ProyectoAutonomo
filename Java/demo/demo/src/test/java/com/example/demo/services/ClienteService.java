package com.example.demo.services;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.models.clienteModels;
import com.example.demo.repositories.ClienteRepositories;

@Service
public class ClienteService {
    @Autowired
    ClienteRepositories clienteRepositories;

    public ArrayList<clienteModels> obtenerClientes(){
        return (ArrayList<clienteModels>) clienteRepositories.findAll();
    }
}

public clienteModels guardarCliente(clienteModels cliente){
    return clienteRepositories.save(cliente);
}