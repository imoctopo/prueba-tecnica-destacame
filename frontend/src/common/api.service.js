import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import {API_URL} from "@/common/config";

const resolved = {
    data: null,
    error: null
}

const APIService = {
    init() {
        Vue.use(VueAxios, axios);
        Vue.axios.defaults.baseURL = API_URL;
    },
    setHeader() {
        Vue.axios.defaults.headers.common["Content-Type"] = "application/json";
    },
    async list(resource) {
        try {
            const res = await Vue.axios.get(`${resource}`);
            resolved.data = res.data;
            resolved.error = null;
        } catch (error) {
            resolved.error = error.response;
            resolved.data = null;
        }
        return resolved;
    },
    async get(resource, id = null) {
        try {
            const res = await Vue.axios.get(`${resource}/${id}`);
            resolved.data = res.data;
            resolved.error = null;
        } catch (error) {
            resolved.error = error.response;
            resolved.data = null;
        }
        return resolved;
    },
    async post(resource, data) {
        try {
            const res = await Vue.axios.post(resource, data);
            resolved.data = res.data;
            resolved.error = null;
        } catch (error) {
            resolved.error = error.response;
            resolved.data = null;
        }
        return resolved;
    },
    async put(resource, id, data) {
        try {
            const res = await Vue.axios.put(`${resource}/${id}`, data);
            resolved.data = res.data;
            resolved.error = null;
        } catch (error) {
            resolved.error = error.response;
            resolved.data = null;
        }
        return resolved;
    },
    async delete(resource, id) {
        try {
            await Vue.axios.delete(`${resource}/${id}`);
            resolved.error = null;
        } catch (error) {
            resolved.error = error.response;
        }
        return resolved;
    }
}
export default APIService;
